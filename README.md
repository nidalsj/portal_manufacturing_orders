# 🏭 Portal Manufacturing Orders

![Odoo Version](https://img.shields.io/badge/Odoo-17.0-blue.svg)
![License: LGPL-3](https://img.shields.io/badge/License-LGPL--3-green.svg)
![Status](https://img.shields.io/badge/Stage-Development-yellow.svg)
![Maintainer](https://img.shields.io/badge/Maintainer-Nidal%20SJ-purple.svg)

**Portal Manufacturing Orders** is an Odoo module that extends the **Customer Portal** to include Manufacturing Orders (MOs).  
It allows portal users or followers to view, search, and download details of Manufacturing Orders directly from the website.

---

## 🚀 Features

### 🧾 Portal List View
- Displays all Manufacturing Orders that the logged-in user follows (`message_partner_ids`).
- Supports **search**, **sort**, and **filter** options:
  - **Search** by Order Name or Product.
  - **Filter** by state: Draft, Confirmed, In Progress, To Close, or Done.
  - **Sort** by Date, Name, or Status.
- Uses the standard Odoo portal layout for consistency.
- Pagination — Added page navigation for large MO lists (e.g., 20 Orders per page).

### 📄 Detailed MO View
- Displays a **form-style page** with key Manufacturing Order details:
  - Product, Quantity, Status, Responsible, Planned Dates, etc.
- Integrated **chatter section** (communication history).
- Includes **breadcrumb navigation** for smooth navigation:
  - `Home / Manufacturing Orders / WH/MO/00012`
- Layout inspired by Odoo’s **Sales Order** portal view.

### 🧰 Sidebar (Portal Layout)
- Sidebar section displays:
  - MO name and current status.
  - Key information such as quantities and responsible person.
  - **Print Production Order** button to download the official MO PDF report.

### 🖨️ Print Production Order
- Integrates with Odoo’s default **`action_report_production_order`**.
- Generates and downloads the “Production Order” PDF used in backend Manufacturing.
- Automatically names the file like:  
  `Production Order - WH-MO00012.pdf`

### 🔒 Access Control
- Only portal users who are **followers** of the MO (`message_partner_ids`) can access it.
- Internal users (with MRP access) can open the same MO in the backend directly.

---

## 🧩 Technical Overview

| Category | Details |
|-----------|----------|
| **Module Name** | `portal_manufacturing_orders` |
| **Version** | 17.0.1.0.0 |
| **Depends On** | `portal`, `mrp`, `website` |
| **Models Used** | `mrp.production` |
| **Main Controller** | `PortalManufacturingOrders` |
| **Portal Routes** | `/my/manufacturing`, `/my/manufacturing/<id>` |
| **Security** | Portal access only (`auth="user"`) |

---

## ⚙️ Installation

1. Copy this module into your Odoo **addons** directory.  
2. Update the app list:
   ```bash
   odoo -u all

## 🖼️ Screenshots

