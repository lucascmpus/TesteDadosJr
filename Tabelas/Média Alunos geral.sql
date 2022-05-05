select 
	round(avg(vídeos),2) as avgVideos,
    round(avg(redações),2) as avgRedação,
    round(avg(questões),2) as avgQuestões,
    round(avg(simulados),2) as avgSimulados,
    round(avg(logins),2) as avgLogins,
    count(*) as qtAlunos
from alunos 	