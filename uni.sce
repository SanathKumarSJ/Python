clc;
clear all;
bits=[1 0 1 0 0 0 1 1 0];
subplot(2,1,1);
plot(bits,'linewidth',1.5);

bitrate=1;
T=length(bits)/bitrate;
n=200;
N=n*length(bits);
dt=T/N;
t=0:dt:T;
x=zeros(1,length(t));
for i=0:length(bits)-1
    if bits(i+1)==1
        x(i*n+1:(i+0.5)*n)=1;
         x((i+0.5)*n+1:(i+1)*n)=0;
    else
        x(i*(n+1):(i+1)*n)=0;
    end
end
subplot(2,1,2);
plot(t,x,'linewidth',3);

axis([0+(end)-0.1 1.1]);
grid on;
title('unipolar rz');
