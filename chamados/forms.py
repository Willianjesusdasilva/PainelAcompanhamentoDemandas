from django import forms
from .models import Registro_de_chamados

ESCOLHAS_HASHTAGS = [
    ('  ', '  '),
    ('#DBA', '#DBA'),
    ('#ERRO', '#ERRO'),
    ('#ERRO #PERFORMANCE', '#ERRO #PERFOMANCE'),
    ('#ANALISECONFIG', '#ANALISECONFIG'),
    ('#SUPORTE', '#SUPORTE'),
    ('#SUPINTERNO', '#SUPINTERNO')
    ]

ESCOLHAS_TIMES = [
    ('', ''),
    ('Alemanha', 'Alemanha'),
    ('Brasil', 'Brasil'),
    ('Japão', 'Japão')
    ]

ESCOLHAS_SITUACOES = [
    ('', ''),
    ('Aceite Final', 'Aceite Final'),
    ('Subsídio Técnico', 'Subsídio Técnico'),
    ('Enc. Monitoramento', 'Enc. Monitoramento'),
    ('Enc. Correção', 'Enc. Correção'),
    ('Enc. DBA', 'Enc. DBA'),
    ('Enc. Outros sistemas', 'Enc. Outros sistemas'),
    ('Recategorização', 'Recategorização')
    ]

ESCOLHAS_COLABORADOR = [
    ('', ''),
    ('DANIEL SAND', 'DANIEL SAND'),
    ('EDUARDA GUIMARÃES', 'EDUARDA GUIMARÃES'),
    ('MAURICIO ROBSON', 'MAURICIO ROBSON'),
    ('OSWALDO MELO', 'OSWALDO MELO'),
    ('PRISCILA FLORES', 'PRISCILA FLORES'),
    ('WILLIAN SILVA', 'WILLIAN SILVA'),
    ('GEORGE ARCEGO', 'GEORGE ARCEGO'),
    ('GUILHERME RECKERS', 'GUILHERME RECKERS'),
    ('PHELIPE ALMEIDA', 'PHELIPE ALMEIDA'),
    ('EVANDRO LUIZ', 'EVANDRO LUIZ'),
    ('MARCOS CRUZ', 'MARCOS CRUZ'),
    ('RAFAELA ROSA', 'RAFAELA ROSA'),
    ('JAQUELINE COSTA', 'JAQUELINE COSTA'),
    ('MARIANA MILANI', 'MARIANA MILANI'),
    ('REIZIELLE RAMOS', 'REIZIELLE RAMOS'),
    ('GUILHERME LUIS', 'GUILHERME LUIS'),
    ('GRASIELLE MENDES', 'GRASIELLE MENDES'),
    ('BRUNO SANTOS', 'BRUNO SANTOS'),
    ('TULIO GUILHERME', 'TULIO GUILHERME'),
    ('JORGE ANDRE', 'JORGE ANDRE')
    ]


class Chamados_form(forms.ModelForm):
    class Meta:
        model = Registro_de_chamados
        fields = ['id_chamado', 'numero_salt', 'data_envio', 'time', 'hashtags', 'situacoes', 'colaborador']
        widgets = {
            'numero_salt': forms.TextInput(attrs={'class': 'form-control'}),
            'data_envio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'situacoes': forms.Select(choices=ESCOLHAS_SITUACOES, attrs={'class': 'form-control'}),
            'time': forms.Select(choices=ESCOLHAS_TIMES, attrs={'class': 'form-control'}),
            'hashtags': forms.Select(choices=ESCOLHAS_HASHTAGS, attrs={'class': 'form-control'}),
            'colaborador': forms.Select(choices=ESCOLHAS_COLABORADOR, attrs={'class': 'form-control'})
            }
