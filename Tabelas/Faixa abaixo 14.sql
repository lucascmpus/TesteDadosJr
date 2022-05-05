select faixa,
		count(faixa)
from alunos
where TempoMatricula <=14
and datacancelamento is not null
group by faixa
order by count(faixa) desc


