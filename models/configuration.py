# -*- coding: utf-8 -*-

from odoo import models, fields, api
import odoo.addons.decimal_precision as dp

class GenderBase(models.Model):
    _name= 'gender'
    _description = "Descripe gender of students and guadrians "

    gender = fields.Char('Gender',  tracking=True  ) 

class IdType(models.Model):
    _name= 'id.type'
    _description = "Descripe Identification type "

    id_type = fields.Char('ID Type',
            tracking=True
        ) 
    
class WorkType(models.Model):
    _name= 'work.type'
    _description = "Descripe work type "

    work_type = fields.Char('Work Type',
            tracking=True
        ) 
    
class KnowUs(models.Model):
    _name= 'know.us'
    _description = "Descripe how you are know about us "

    know_us = fields.Char('Know Us',
            tracking=True
        )   
class StudentStatus(models.Model):
    _name= 'student.status'
    _description = "Descripe status of student "

    name = fields.Char('Student Status',
            tracking=True
        )   
      
class DiscouontType(models.Model):
    _name= 'discount.type'
    _description = "Discount types  "

    discount_type = fields.Char('Discount Type',
            tracking=True
        ) 
    
class Discounts(models.Model):
    _name= 'discounts'
    _description = "Discounts "

    name = fields.Char('Name',
            tracking=True
        )
    ratio = fields.Char('Ratio',
            tracking=True
        )
    
    discount_type = fields.Many2one('discount.type',
            tracking=True
        )
    discription = fields.Char('Discription',
            tracking=True
        ) 
    company_id = fields.Many2one('res.company', string="Company", default=1)
    
class SchoolssBase(models.Model):
    _name= 'schools'
    _description = "Descripe gender of students and guadrians "

    same = fields.Char('schools',  tracking=True  ) 

    
class StudentsBase(models.Model):
    _name= 'students'
    _description = "Descripe students  "

    name = fields.Char('students',  tracking=True  ) 

    
class GuardianBase(models.Model):
    _name= 'guardians'
    _description = "Descripe guadrians of students   "

    name = fields.Char('guardians',  tracking=True  ) 
    
class TracksBase(models.Model):
    _name= 'tracks'
    _description = "Descripe Tracks of students "

    name = fields.Char('Tracks',  tracking=True  ) 
    
class SectionsBase(models.Model):
    _name= 'sections'
    _description = "Descripe Sections of students  "

    name = fields.Char('Sections',  tracking=True  ) 

class StagesBase(models.Model):
    _name= 'stages'
    _description = "Descripe Stages of students  "

    name = fields.Char('Stages',  tracking=True  ) 
    is_secondary = fields.Char('Stages',  tracking=True  ) 
    Section_id = fields.Many2one('sections',  tracking=True  ) 
    track_id = fields.Many2one('tracks',  tracking=True  ) 

class ClassesBase(models.Model):
    _name= 'classes'
    _description = "Descripe Stages of students  "

    name = fields.Char('Class',  tracking=True  ) 
    stage_id = fields.Char('stages',  tracking=True  ) 
    Section_id = fields.Many2one('sections',  tracking=True  ) 
    track_id = fields.Many2one('tracks',  tracking=True  ) 

class SecondryMajorsBase(models.Model):
    _name= 'secondry.majors'
    _description = "Descripe Stages of students  "

    name = fields.Char('Class',  tracking=True  ) 
    stage_id = fields.Char('stages',  tracking=True  ) 
    Section_id = fields.Many2one('sections',  tracking=True  ) 
    track_id = fields.Many2one('tracks',  tracking=True  ) 

class ExSchools(models.Model):

    _name= 'extra.schools'
    _description = "Descripe Stages of students  "

    name = fields.Char('ExSchools Name',  tracking=True  ) 
    outside_madinah = fields.Boolean('Outside Madinah',  tracking=True  ) 

class Years(models.Model):

    _name= 'years'
    _description = "Descripe Years of students  "

    name = fields.Char('Name',  tracking=True  ) 

class Fees(models.Model):

    _name= 'fees'
    _description = "Descripe Fees of students  "

    name = fields.Char('Name',  tracking=True  ) 
    stage_id = fields.Char('stages',  tracking=True  ) 
    product_id = fields.Char('product.template',  tracking=True  ) 

class ProductsStudents(models.Model):

    _inherit= 'product.template'
    _description = "Descripe Products of students  "
