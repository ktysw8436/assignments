score = ['D','D+','C','C+','B','B+','A','A+']
stop = 0
cnt = [0,0]
avg = 0
cntf = [0,0]
cntp = [0,0,0,0]
print('학점과 성적 입력, 종료 시 exit 입력')
while(stop != 1):
    subject = input().split()
    if subject[0] == 'exit':
        stop = 1
    elif subject[1] == 'F':
        cnt[0] += 1
        cnt[1] += int(subject[0])
        cntf[0] += 1
        cntf[1] += int(subject[0])
    elif subject[1] == 'P':
        cnt[0] += 1
        cntp[0] += int(subject[0])
        cntp[2] += 1
    elif subject[1] == 'NP':
        cntp[1] += int(subject[0])
        cntp[3] += 1
    else:
        cnt[0] += 1
        cnt[1] += int(subject[0])
        avg += (score.index(subject[1]) * 0.5 + 1.0) * int(subject[0])
print('총 이수 학점: '+str(cnt[1] + cntp[0])+'학점')
print('총 이수 과목: '+str(cnt[0])+'과목')
print('평균 평점: '+str(avg / cnt[1]))
print('F학점 과목 수: '+str(cntf[0]))
print("F 학점 수: "+str(cntf[1])+'학점')
print("총 P/NP 과목 수: "+str(cntp[2] + cntp[3])+'과목')
print('총 P/NP 학점 수: '+str(cntp[0] + cntp[1])+'학점')
print("Pass 과목 수: "+str(cntp[2])+'과목')
print('Pass 학점 수: '+str(cntp[0])+'학점')
print("Non-Pass 과목 수: "+str(cntp[3])+'과목')
print('Non-Pass 학점 수: '+str(cntp[1])+'학점')

    