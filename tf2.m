%2-2 第一问
% num=[1 7 24 24];
% den=[1 10 35 50 24];
% G1=tf(num,den)
% [A B C D]=tf2ss(num,den)
% [Z,P,K]=tf2zp(num,den)
% [R P H]=residue(num,den)
% G2=ss(A,B,C,D)
% G3=zpk(Z,P,K)
% [a,b]=residue(R,P,H)

%第二问
% A=[2.25 -5 -1.25 -0.5;2.25 -4.25 -1.25 -0.25;0.25 -0.5 -1.25 -1;1.25 -1.75 -0.25 -0.75]
% B=[4 ;2 ;2 ;0] 
% C=[0 2 0 2]
% D=[0]
% [num,den]=ss2tf(A,B,C,D)
% G1=tf(num,den)
% [Z P K]=ss2zp(A,B,C,D)
% G2=zpk(Z,P,K)
% [R P H]=residue(num,den)

%2-7
%求多项式的解
r=[1 3.4 16.35];
roots(r)
Z=[-20]
P=[0 -4.6 -1.7+3.6688i -1.7-3.6688i]
K=[5]
[num,den]=zp2tf(Z,P,K)  
G1=tf(num,den)%开环传递函数
G2 = feedback(G1,1,-1) %不能直接用G2=G1/（1+G1），要用feedback求闭环传递函数
num1=[5 100];
den1=[1 8 31.99 80.21 100];
[Z1 P1 K1]=tf2zp(num1,den1)
[A B C D]=tf2ss(num1,den1)

