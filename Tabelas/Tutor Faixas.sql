select tutor,
		count(tutor)
from alunos
where faixa like '%preta%'
group by tutor
