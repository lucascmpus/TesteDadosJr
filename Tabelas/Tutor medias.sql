select tutor,
		count(tutor),
		round(avg(vídeos),2) as avgVideos,
		round(avg(redações),2) as avgRedação,
		round(avg(questões),2) as avgQuestões,
		round(avg(simulados),2) as avgSimulados,
		round(avg(logins),2) as avgLogins
from alunos 
group by tutor