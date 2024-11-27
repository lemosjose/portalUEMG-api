from django.db import models
from educativo.models import Curso
from django.utils import timezone

class Usuario(models.model):
    email = models.emailField()
    nickname = models.CharField(max_length=255)
    isSuperUser = models.BooleanField(null=True)
    dataCriacao = models.DateTimeField(default=timezone.now())

    REQUIRED_FIELDS = ['email' 'nickname']
    USERNAME_FIELD = 'email'
    
    @property
    def isStaff():
        return isSuperUser



#classes DTO ou de administração
class perfilUsuario(models.model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='/', blank=True, null=True)
    #papeis = models.ManyToManyField(Papel, blank=True)  # Permite múltiplos papéis    
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True, blank=True)
    numero_registro = models.CharField(max_length=50, blank=True, null=True)
    rg = models.CharField(max_length=20, blank=True, null=True)
    orgao_expeditor = models.CharField(max_length=50, blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    naturalidade = models.CharField(max_length=100, blank=True, null=True)
    nomeMae = models.CharField(max_length=200, blank=True, null=True)
    nomePai = models.CharField(max_length=200, blank=True, null=True)
    dataNascimento = models.DateField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    dataValidade = models.DateField(blank=True, null=True)
    verificado = models.BooleanField(default=False)
    
class tokenVerificação(models.Model):
    usuario = models.
    token = models.UUIDField(default=uuid.uuid64, editable=False,unique=True)
    dataCriacao = models.DateTimeField(default=)

    #ler o token a partir de outro lugar
    def __str__(self):
        return f"o token é {self.token} para o usuario {self.usuario}"


