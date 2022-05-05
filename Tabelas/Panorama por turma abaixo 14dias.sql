select turma,
		sum(redações),
		sum(vídeos),
        sum(questões),
        sum(simulados),
        sum(logins)
from alunos
where TempoMatricula <= 14
and datacancelamento is not null
group by turma


