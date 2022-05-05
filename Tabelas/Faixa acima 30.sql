select faixa,
		count(faixa)
from alunos
where TempoMatricula >=30
and tempomatricula <=60
and datacancelamento is not null
group by faixa
order by count(faixa) desc


