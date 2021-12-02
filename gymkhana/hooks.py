# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "gymkhana"
app_title = "gymkhana"
app_publisher = "Shahzad Naser"
app_description = "gymkhana"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "shahzadnaser1122@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/gymkhana/css/gymkhana.css"
# app_include_js = "/assets/gymkhana/js/gymkhana.js"

# include js, css files in header of web template
# web_include_css = "/assets/gymkhana/css/gymkhana.css"
# web_include_js = "/assets/gymkhana/js/gymkhana.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Payment Entry" : "public/js/payment_entry.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "gymkhana.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "gymkhana.install.before_install"
# after_install = "gymkhana.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "gymkhana.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"gymkhana.tasks.all"
# 	],
# 	"daily": [
# 		"gymkhana.tasks.daily"
# 	],
# 	"hourly": [
# 		"gymkhana.tasks.hourly"
# 	],
# 	"weekly": [
# 		"gymkhana.tasks.weekly"
# 	]
# 	"monthly": [
# 		"gymkhana.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "gymkhana.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "gymkhana.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "gymkhana.task.get_dashboard_data"
# }

doctypes_list = ["Customer","Payment Entry"]

fixtures = [
    {"doctype": "Custom Script", "filters": [
        [
            "dt", "in", doctypes_list
        ]
    ]},
    {"doctype": "Property Setter", "filters": [
        [
            "doc_type", "in", doctypes_list
        ]
    ]},
    {"doctype": "Custom Field", "filters": [
        [
            "dt", "in", doctypes_list
        ]
    ]}
]
