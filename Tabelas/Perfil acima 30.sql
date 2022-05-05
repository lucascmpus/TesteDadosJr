select Perfil,
		count(perfil) as qtPerfil
from alunos
where tempomatricula >=30
and tempomatricula <= 60
and datacancelamento is not null
group by perfil
order by count(perfil) desc

