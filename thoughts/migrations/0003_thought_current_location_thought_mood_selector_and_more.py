# Generated by Django 4.1.7 on 2023-03-18 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thoughts', '0002_alter_thought_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='thought',
            name='current_location',
            field=models.TextField(default='earth', max_length=25),
        ),
        migrations.AddField(
            model_name='thought',
            name='mood_selector',
            field=models.CharField(choices=[('normal', 'Normal'), ('sad', 'Sad'), ('happy', 'Happy'), ('anxious', 'Anxious'), ('romantic', 'Romantic'), ('hopeful', 'Hopeful'), ('angry', 'Angry'), ('lonely', 'Lonely'), ('cheerful', 'Cheerful'), ('excited', 'Excited')], default='normal', max_length=32),
        ),
        migrations.AlterField(
            model_name='thought',
            name='content',
            field=models.TextField(max_length=300),
        ),
    ]
