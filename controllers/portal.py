from odoo import http, _
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.exceptions import AccessError, MissingError

class PortalManufacturingOrders(CustomerPortal):

    def _prepare_manufacturing_orders_domain(self, search=None, search_in='all'):
        domain = []
        
        if search and search_in:
            if search_in == 'name':
                domain = [('name', 'ilike', search)]
            elif search_in == 'product':
                domain = [('product_id', 'ilike', search)]
            elif search_in == 'all':
                domain = ['|', ('name', 'ilike', search), ('product_id', 'ilike', search)]
        return domain

    @http.route(['/my/manufacturing'], type='http', auth="user", website=True)
    def portal_my_manufacturing_orders(self, sortby=None, filterby=None, search=None, search_in='all', **kw):
        values = self._prepare_portal_layout_values()
        ManufacturingOrder = request.env['mrp.production'].sudo()
        partner = request.env.user.partner_id
        domain = [('message_partner_ids', 'in', [partner.id])]

        # Sort
        searchbar_sortings = {
            'date': {'label': _('Newest'), 'order': 'create_date desc'},
            'name': {'label': _('Name'), 'order': 'name'},
            'state': {'label': _('Status'), 'order': 'state'},
        }
        sortby = sortby or 'date'
        order = searchbar_sortings[sortby]['order']

        # Filter
        searchbar_filters = {
            'all': {'label': _('All'), 'domain': []},
            'draft': {'label': _('Draft'), 'domain': [('state', '=', 'draft')]},
            'confirmed': {'label': _('Confirmed'), 'domain': [('state', '=', 'confirmed')]},
            'progress': {'label': _('In Progress'), 'domain': [('state', '=', 'progress')]},
            'to_close': {'label': _('To Close'), 'domain': [('state', '=', 'to_close')]},
            'done': {'label': _('Done'), 'domain': [('state', '=', 'done')]},
        }
        filterby = filterby or 'all'
        domain += searchbar_filters[filterby]['domain']

        # Search
        searchbar_inputs = {
            'all': {'input': 'all', 'label': _('Search All')},
            'name': {'input': 'name', 'label': _('Search Order Name')},
            'product': {'input': 'product', 'label': _('Search Product')},
        }
        search_domain = self._prepare_manufacturing_orders_domain(search, search_in)
        domain += search_domain
        manufacturing_orders = ManufacturingOrder.search(domain, order=order)

        values.update({
            'manufacturing_orders': manufacturing_orders,
            'page_name': 'manufacturing_orders',
            'default_url': '/my/manufacturing',
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby,
            'searchbar_filters': searchbar_filters,
            'filterby': filterby,
            'searchbar_inputs': searchbar_inputs,
            'search_in': search_in,
            'search': search,
        })
        
        return request.render("portal_manufacturing_orders.portal_manufacturing_list", values)
    
    @http.route(['/my/manufacturing/<int:order_id>'], type='http', auth="user", website=True)
    def portal_my_manufacturing_order(self, order_id=None, access_token=None, **kw):
        try:
            order_sudo = self._document_check_access('mrp.production', order_id, access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        values = {
            'page_name': 'manufacturing_order',
            'manufacturing_order': order_sudo,
        }
        
        return request.render("portal_manufacturing_orders.portal_manufacturing_order_page", values)
    
