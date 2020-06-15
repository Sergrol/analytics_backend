# Generated by Django 2.2.6 on 2020-04-25 20:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dataprocessing', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Competence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=1024, unique=True)),
                ('name', models.CharField(max_length=1024, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DisciplineSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, unique=True, verbose_name='Раздел')),
            ],
        ),
        migrations.CreateModel(
            name='EvaluationTool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=1024, verbose_name='Тип оценочного средства')),
                ('name', models.CharField(max_length=1024, unique=True, verbose_name='Наименование оценочного средства')),
                ('description', models.CharField(max_length=1024, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='FieldOfStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=1024, unique=True, verbose_name='Шифр и название ОП')),
                ('qualification', models.CharField(choices=[('primary_vocational_education', 'Primary vocational education'), ('secondary_vocational_education', 'Secondary vocational education'), ('bachelor', 'Bachelor'), ('specialist', 'Specialist'), ('master', 'Master')], max_length=1024, verbose_name='Квалификация')),
                ('education_form', models.CharField(choices=[('internal', 'Internal'), ('extramural', 'Extramural')], max_length=1024, verbose_name='Форма обучения')),
            ],
        ),
        migrations.CreateModel(
            name='FieldOfStudyWorkProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competence', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='workprogramsapp.Competences', verbose_name='Компетенции')),
                ('field_of_study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workprogramsapp.FieldOfStudy', verbose_name='Образовательная программа')),
            ],
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=1024, unique=True)),
                ('name', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='OutcomesOfWorkProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('masterylevel', models.CharField(choices=[('1', 'low'), ('2', 'average'), ('3', 'high')], default=1, max_length=1, verbose_name='Уровень')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataprocessing.Items', verbose_name='Постреквизит')),
            ],
        ),
        migrations.CreateModel(
            name='PrerequisitesOfWorkProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('masterylevel', models.CharField(choices=[('1', 'low'), ('2', 'average'), ('3', 'high')], default=1, max_length=1, verbose_name='Уровень')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataprocessing.Items', verbose_name='Пререквизит')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_of_study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workprogramsapp.FieldOfStudy')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024, verbose_name='Название')),
                ('hoursFirstSemester', models.IntegerField(blank=True, null=True, verbose_name='Количество часов в 1 семестре')),
                ('hoursSecondSemester', models.IntegerField(blank=True, null=True, verbose_name='Количество часов в 2 семестре')),
                ('goals', models.CharField(max_length=1024, verbose_name='Цели освоения')),
                ('result_goals', models.CharField(max_length=1024, verbose_name='Результаты освоения')),
                ('field_of_studies', models.ManyToManyField(through='workprogramsapp.FieldOfStudyWorkProgram', to='workprogramsapp.FieldOfStudy', verbose_name='Предметная область')),
                ('outcomes', models.ManyToManyField(related_name='WorkProgramOutcomes', through='workprogramsapp.OutcomesOfWorkProgram', to='dataprocessing.Items', verbose_name='Постреквизиты')),
                ('prerequisites', models.ManyToManyField(blank=True, null=True, related_name='WorkProgramPrerequisites', through='workprogramsapp.PrerequisitesOfWorkProgram', to='dataprocessing.Items', verbose_name='Пререквизиты')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=1024, unique=True, verbose_name='Номер')),
                ('description', models.CharField(max_length=1024, verbose_name='Описание')),
                ('discipline_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workprogramsapp.DisciplineSection', verbose_name='Раздел')),
            ],
        ),
        migrations.CreateModel(
            name='RouteComposition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.PositiveSmallIntegerField()),
                ('field_of_study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workprogramsapp.FieldOfStudy')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workprogramsapp.Route')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('work_program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workprogramsapp.WorkProgram')),
            ],
            options={
                'unique_together': {('route', 'user', 'work_program', 'field_of_study')},
            },
        ),
        migrations.AddField(
            model_name='route',
            name='work_programs',
            field=models.ManyToManyField(through='workprogramsapp.RouteComposition', to='workprogramsapp.WorkProgram'),
        ),
        migrations.AddField(
            model_name='prerequisitesofworkprogram',
            name='workprogram',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workprogramsapp.WorkProgram', verbose_name='Рабочая программа'),
        ),
        migrations.AddField(
            model_name='outcomesofworkprogram',
            name='workprogram',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workprogramsapp.WorkProgram', verbose_name='Рабочая программа'),
        ),
        migrations.CreateModel(
            name='IndicatorWorkProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('knowledge', models.CharField(max_length=1024)),
                ('skills', models.CharField(max_length=1024)),
                ('proficiency', models.CharField(max_length=1024)),
                ('competence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workprogramsapp.Competences')),
                ('indicator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workprogramsapp.Indicator')),
                ('work_program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workprogramsapp.WorkProgram')),
            ],
            options={
                'unique_together': {('competence', 'work_program', 'indicator')},
            },
        ),
        migrations.AddField(
            model_name='indicator',
            name='work_programs',
            field=models.ManyToManyField(through='workprogramsapp.IndicatorWorkProgram', to='workprogramsapp.WorkProgram'),
        ),
        migrations.AddField(
            model_name='fieldofstudyworkprogram',
            name='work_program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workprogramsapp.WorkProgram', verbose_name='Рабочая программа'),
        ),
        migrations.AddField(
            model_name='disciplinesection',
            name='evaluation_tools',
            field=models.ManyToManyField(to='workprogramsapp.EvaluationTool', verbose_name='Фонды оценочных средств'),
        ),
        migrations.AddField(
            model_name='disciplinesection',
            name='work_program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workprogramsapp.WorkProgram', verbose_name='Рабочая программа'),
        ),
        migrations.CreateModel(
            name='CompetenceIndicator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workprogramsapp.Competences')),
                ('field_of_study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workprogramsapp.FieldOfStudy')),
                ('indicator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workprogramsapp.Indicator')),
            ],
            options={
                'unique_together': {('competence', 'indicator', 'field_of_study')},
            },
        ),
        migrations.AddField(
            model_name='competence',
            name='field_of_study',
            field=models.ManyToManyField(to='workprogramsapp.FieldOfStudy'),
        ),
        migrations.AddField(
            model_name='competence',
            name='indicators',
            field=models.ManyToManyField(through='workprogramsapp.CompetenceIndicator', to='workprogramsapp.Indicator'),
        ),
        migrations.AddField(
            model_name='competence',
            name='work_program',
            field=models.ManyToManyField(to='workprogramsapp.WorkProgram'),
        ),
        migrations.AlterUniqueTogether(
            name='fieldofstudyworkprogram',
            unique_together={('competence', 'work_program', 'field_of_study')},
        ),
    ]
