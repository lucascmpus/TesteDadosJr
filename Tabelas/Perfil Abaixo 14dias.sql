select Perfil,
		count(perfil) as qtPerfil
from alunos
where tempomatricula <= 14
and datacancelamento is not null
group by perfil

