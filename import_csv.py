import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database="kuadro1"
)

mycursor = mydb.cursor()

file = open("database1.csv", "r", encoding="utf-8")
lines = file.readlines()
val = []
for line_number,line in enumerate(lines):
    if line_number > 0:
        valores = line.split(",")
        
        #IDAluno,Turma,Plano,Faixa,Redações,Vídeos,Questões,DataMatriculada,Simulados,Tutor,Logins,Perfil,DataCancelamentp,DataNascimento,AcessoAte
        id_aluno = valores[0]
        turma = valores[1]
        plano= valores[2] 
        faixa= valores[3]
        redacoes= valores[4] 
        videos= valores[5] 
        questoes= valores[6] 
        data_matriculada = None if valores[7] == 'N/A' else datetime.strptime(valores[7], '%d/%m/%Y %H:%M:%S')
        simulados= valores[8] 
        tutor= valores[9] 
        logins= valores[10] 
        perfil= valores[11] 
        data_cancelamento= None if valores[12] == 'N/A' else datetime.strptime(valores[12], '%d/%m/%Y %H:%M:%S') 
        tempo_matricula = valores[13]
        data_nascimento= None if valores[14] == 'N/A' else datetime.strptime(valores[14], '%d/%m/%Y %H:%M:%S')
        acesso_ate= None if valores[15] == 'N/A' else datetime.strptime(valores[15][0:19], '%d/%m/%Y %H:%M:%S')

    
        val.append((id_aluno,turma,plano,faixa,redacoes,videos,questoes,data_matriculada if data_matriculada == None else data_matriculada.strftime("%Y-%m-%d %H:%M:%S"),simulados,tutor,logins,perfil,data_cancelamento if data_cancelamento == None else data_cancelamento.strftime("%Y-%m-%d %H:%M:%S"),tempo_matricula,data_nascimento if data_nascimento == None else data_nascimento.strftime("%Y-%m-%d %H:%M:%S"),acesso_ate if acesso_ate == None else acesso_ate.strftime("%Y-%m-%d %H:%M:%S")))

sql = "INSERT INTO Alunos (IdAluno,Turma,Plano,Faixa,Redações,Vídeos,Questões,DataMatriculada,Simulados,Tutor,Logins,Perfil,DataCancelamento,TempoMatricula, DataNascimento,AcessoAte) VALUES (%s, %s,%s, %s,%s, %s, %s, %s,%s, %s,%s, %s,%s, %s, %s, %s)"
mycursor.executemany(sql, val)

mydb.commit()

file.close()  