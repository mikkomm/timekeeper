# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Chore'
        db.create_table(u'chronos_chore', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='chore_owner', to=orm['auth.User'])),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='chore_project', to=orm['chronos.Project'])),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(related_name='chore_task', to=orm['chronos.Task'])),
            ('reference', self.gf('django.db.models.fields.related.ForeignKey')(related_name='chore_reference', to=orm['chronos.Reference'])),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('edited_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='chore_created_by', to=orm['auth.User'])),
            ('edited_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='chore_edited_by', to=orm['auth.User'])),
        ))
        db.send_create_signal(u'chronos', ['Chore'])


    def backwards(self, orm):
        # Deleting model 'Chore'
        db.delete_table(u'chronos_chore')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'chronos.chore': {
            'Meta': {'object_name': 'Chore'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'chore_created_by'", 'to': u"orm['auth.User']"}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'edited_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'chore_edited_by'", 'to': u"orm['auth.User']"}),
            'edited_date': ('django.db.models.fields.DateTimeField', [], {}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'chore_owner'", 'to': u"orm['auth.User']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'chore_project'", 'to': u"orm['chronos.Project']"}),
            'reference': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'chore_reference'", 'to': u"orm['chronos.Reference']"}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'chore_task'", 'to': u"orm['chronos.Task']"})
        },
        u'chronos.project': {
            'Meta': {'object_name': 'Project'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'project_created_by'", 'to': u"orm['auth.User']"}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'edited_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'project_edited_by'", 'to': u"orm['auth.User']"}),
            'edited_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'chronos.reference': {
            'Meta': {'object_name': 'Reference'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reference_created_by'", 'to': u"orm['auth.User']"}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {}),
            'edited_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reference_edited_by'", 'to': u"orm['auth.User']"}),
            'edited_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reference_project'", 'null': 'True', 'to': u"orm['chronos.Project']"})
        },
        u'chronos.task': {
            'Meta': {'object_name': 'Task'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'task_created_by'", 'to': u"orm['auth.User']"}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {}),
            'edited_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'task_edited_by'", 'to': u"orm['auth.User']"}),
            'edited_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['chronos']