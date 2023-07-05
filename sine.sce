clear all;
bits=[1 1 0 0 1 0 0 1];
pi=3.1412;
subplot(2,1,1);
plot(bits,'linewidth',1.5);
bitrate=1;
bitnum=[1:length(bits)]
T=1/bitrate;
Tf=length(bits)*T;
f=1/(2*T);
n=200;
N=n*length(bits);
dt=Tf/N;
signal=[];
u=0:T/200:T;
for i=0:length(bits)-1
    if bits(i+1)==1
    p=sin(2*pi*f*u);
else
    p=-sin(2*pi*f*u);
end
signal=[signal,p]
end
t=linspace(0,Tf,length(signal));
subplot(2,1,2);
plot(signal,'linewidth',1.5);
plot(signal,'linewidth',1.5);
title('half sine pulse')
xlabel('time in sec');
ylabel('amplitude in v');
   
