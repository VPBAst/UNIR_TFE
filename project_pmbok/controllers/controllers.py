# -*- coding: utf-8 -*-
# from odoo import http


# class ProjectPmbok(http.Controller):
#     @http.route('/project_pmbok/project_pmbok', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_pmbok/project_pmbok/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_pmbok.listing', {
#             'root': '/project_pmbok/project_pmbok',
#             'objects': http.request.env['project_pmbok.project_pmbok'].search([]),
#         })

#     @http.route('/project_pmbok/project_pmbok/objects/<model("project_pmbok.project_pmbok"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_pmbok.object', {
#             'object': obj
#         })
