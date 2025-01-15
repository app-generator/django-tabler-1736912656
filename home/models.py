# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Estudante(models.Model):

    #__Estudante_FIELDS__
    matricula = models.CharField(max_length=255, null=True, blank=True)
    nome = models.CharField(max_length=255, null=True, blank=True)
    endereco = models.CharField(max_length=255, null=True, blank=True)
    numero = models.CharField(max_length=255, null=True, blank=True)
    complemento = models.CharField(max_length=255, null=True, blank=True)
    bairro = models.CharField(max_length=255, null=True, blank=True)
    uf = models.CharField(max_length=255, null=True, blank=True)
    municipio = models.CharField(max_length=255, null=True, blank=True)
    cep = models.CharField(max_length=255, null=True, blank=True)
    telefone_fixo = models.CharField(max_length=255, null=True, blank=True)
    telefone_celular = models.CharField(max_length=255, null=True, blank=True)
    telefone_outro = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    banco = models.CharField(max_length=255, null=True, blank=True)
    tipo_conta = models.CharField(max_length=255, null=True, blank=True)
    numero_conta = models.CharField(max_length=255, null=True, blank=True)
    agencia = models.CharField(max_length=255, null=True, blank=True)
    operacao = models.CharField(max_length=255, null=True, blank=True)
    pcd = models.BooleanField()
    tipo_deficiencia = models.CharField(max_length=255, null=True, blank=True)
    indigena = models.BooleanField()
    quilombola = models.BooleanField()
    etnia_comunidade = models.CharField(max_length=255, null=True, blank=True)

    #__Estudante_FIELDS__END

    class Meta:
        verbose_name        = _("Estudante")
        verbose_name_plural = _("Estudante")


class Ingressoestudante(models.Model):

    #__Ingressoestudante_FIELDS__
    matricula = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    ano_periodo_ingresso = models.CharField(max_length=255, null=True, blank=True)
    forma_ingresso = models.CharField(max_length=255, null=True, blank=True)
    cola_grau = models.BooleanField()
    ingresso_judicial = models.BooleanField()
    preferencia_curso_ingresso = models.CharField(max_length=255, null=True, blank=True)
    especificidade_forma_ingresso = models.CharField(max_length=255, null=True, blank=True)
    categoria_ingresso = models.CharField(max_length=255, null=True, blank=True)
    opcao_participacao = models.CharField(max_length=255, null=True, blank=True)
    mes_ano_processo_seletivo = models.CharField(max_length=255, null=True, blank=True)
    opcao_aprovacao = models.CharField(max_length=255, null=True, blank=True)
    matriz_curricular = models.CharField(max_length=255, null=True, blank=True)
    curso = models.CharField(max_length=255, null=True, blank=True)
    opcao_instrumento = models.CharField(max_length=255, null=True, blank=True)

    #__Ingressoestudante_FIELDS__END

    class Meta:
        verbose_name        = _("Ingressoestudante")
        verbose_name_plural = _("Ingressoestudante")


class Unidadeacademica(models.Model):

    #__Unidadeacademica_FIELDS__
    codigo_ua = models.CharField(max_length=255, null=True, blank=True)
    nome_ua = models.CharField(max_length=255, null=True, blank=True)
    email_setor = models.CharField(max_length=255, null=True, blank=True)
    telefone_setor = models.CharField(max_length=255, null=True, blank=True)
    site = models.CharField(max_length=255, null=True, blank=True)
    localizacao = models.CharField(max_length=255, null=True, blank=True)

    #__Unidadeacademica_FIELDS__END

    class Meta:
        verbose_name        = _("Unidadeacademica")
        verbose_name_plural = _("Unidadeacademica")


class Direcaoua(models.Model):

    #__Direcaoua_FIELDS__
    unidade_academica = models.ForeignKey(UnidadeAcademica, on_delete=models.CASCADE)
    nome_diretor_ua = models.CharField(max_length=255, null=True, blank=True)
    telefone_diretor_ua = models.CharField(max_length=255, null=True, blank=True)
    email_diretor_ua = models.CharField(max_length=255, null=True, blank=True)
    nome_vice_diretor_ua = models.CharField(max_length=255, null=True, blank=True)
    email_vice_diretor_ua = models.CharField(max_length=255, null=True, blank=True)
    telefone_vice_diretor_ua = models.CharField(max_length=255, null=True, blank=True)

    #__Direcaoua_FIELDS__END

    class Meta:
        verbose_name        = _("Direcaoua")
        verbose_name_plural = _("Direcaoua")


class Coordadmua(models.Model):

    #__Coordadmua_FIELDS__
    nome_coord_adm_ua = models.CharField(max_length=255, null=True, blank=True)
    email_coord_adm_ua = models.CharField(max_length=255, null=True, blank=True)
    telefone_coord_adm_ua = models.CharField(max_length=255, null=True, blank=True)
    nome_vice_coord_adm_ua = models.CharField(max_length=255, null=True, blank=True)
    email_vice_coord_adm_ua = models.CharField(max_length=255, null=True, blank=True)
    telefone_vice_coord_adm_ua = models.CharField(max_length=255, null=True, blank=True)
    unidadeacademica = models.ForeignKey(UnidadeAcademica, on_delete=models.CASCADE)

    #__Coordadmua_FIELDS__END

    class Meta:
        verbose_name        = _("Coordadmua")
        verbose_name_plural = _("Coordadmua")


class Cpeua(models.Model):

    #__Cpeua_FIELDS__
    nome_cpe = models.CharField(max_length=255, null=True, blank=True)
    telefone_cpe = models.CharField(max_length=255, null=True, blank=True)
    email_cpe = models.CharField(max_length=255, null=True, blank=True)
    nome_vice_cpe = models.CharField(max_length=255, null=True, blank=True)
    telefone_vice_cpe = models.CharField(max_length=255, null=True, blank=True)
    email_vice_cpe = models.CharField(max_length=255, null=True, blank=True)
    unidade_academica = models.ForeignKey(UnidadeAcademica, on_delete=models.CASCADE)

    #__Cpeua_FIELDS__END

    class Meta:
        verbose_name        = _("Cpeua")
        verbose_name_plural = _("Cpeua")


class Cursos(models.Model):

    #__Cursos_FIELDS__
    nome_coordenador = models.CharField(max_length=255, null=True, blank=True)
    email_coordenador = models.CharField(max_length=255, null=True, blank=True)
    telefone_coordenador = models.CharField(max_length=255, null=True, blank=True)
    nome_vice_coordenador = models.CharField(max_length=255, null=True, blank=True)
    email_vice_coordenador = models.CharField(max_length=255, null=True, blank=True)
    telefone_vice_coordenador = models.CharField(max_length=255, null=True, blank=True)
    email_setor = models.CharField(max_length=255, null=True, blank=True)
    telefone_setor = models.CharField(max_length=255, null=True, blank=True)
    unidade_academica = models.ForeignKey(UnidadeAcademica, on_delete=models.CASCADE)

    #__Cursos_FIELDS__END

    class Meta:
        verbose_name        = _("Cursos")
        verbose_name_plural = _("Cursos")



#__MODELS__END
