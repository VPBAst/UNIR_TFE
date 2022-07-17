from odoo import models, fields, api

class ActaDeProyecto(models.Model):
    _name = 'project_pmbok.ActaDeProyecto'
    _description = 'Modelo de datos que incluye las propiedades o campos de un acta de proyecto'

    # Campos del documento/entregable Acta de proyecto #

    estadoDocumento =  fields.Selection(
        selection=[
            ('draft', 'Borrador'),
            ('confirm', 'Confirmado')
        ],
        string='Estado del documento',
        required=True,
        readonly=True
    )
    projectTitle = fields.Char(string='Titulo del proyecto', required=True)
    datePrepared = fields.Date(string='Fecha de creación', required=True)
    projectManager = fields.Char(string='Jefe del proyecto', required=True)
    projectPurpose = fields.Text(string='Propósito del proyecto', required=True)
    highLevelProjectDescription = fields.Text(string='Descripcion alto-nivel del proyecto', required=True)

    # Relaciones con otras entidades (Interesados, Objetivos, Hitos) #

    stakeHolders = fields.One2Many('project_pmbok.Interesado', 'actaproyecto_id', string='Interesados')
    projectObjetives= fields.One2Many('project_pmbok.ObjetivoProyecto', 'actaproyecto_id', string='Objetivos')
    summaryMilestones= fields.One2Many('project_pmbok.HitoProyecto', 'actaproyecto_id', string='Hitos')
    


class Interesado(models.Model):
    _name = 'project_pmbok.Interesado'
    _description = 'Modelo de datos que representa un interesado (stakeHolder)'
    nombre = fields.Char(string='Nombre del interesado', required=True)
    # Relacion con entidad ActaDeProyecto #
    actaproyecto_id = fields.Many2One('project_pmbok.ActaDeProyecto', string='Acta Proyecto')

class ObjetivoProyecto(models.Model):
     _name = 'project_pmbok.ObjetivoProyecto'
    _description = 'Modelo de datos que representa un objetivo de proyecto'
     nombre = fields.Char(string='Nombre del objetivo', required=True)
     descripcion = fields.Char(string='Descripcion del objetivo', required=True)
     # Relacion con entidad ActaDeProyecto #
     actaproyecto_id = fields.Many2One('project_pmbok.ActaDeProyecto', string='Acta Proyecto')

class HitoProyecto(models.Model):
     _name = 'project_pmbok.HitoProyecto'
    _description = 'Modelo de datos que representa un hito de proyecto'
     nombre = fields.Char(string='Nombre del hito', required=True)
     descripcion = fields.Char(string='Descripcion del hito', required=True)
     fechaHito = fields.Date(string='Fecha estimada del hito', required=True)
     # Relacion con entidad ActaDeProyecto #
     actaproyecto_id = fields.Many2One('project_pmbok.ActaDeProyecto', string='Acta Proyecto')