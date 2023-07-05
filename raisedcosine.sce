clc;
bit=[1 1 0 0 1 0 0 1];
bitrate=1;
bitnum=[1:length(bit)]
Tf=length(bit)/bitrate;
n=200;
N=n*length(bit);
df=Tf/N;
u=0:df:Tf;
a=0.3
T=1;
t=u-T/2;

for i=0;length(bit)-1;
    if bit(i+1)==1
        num1=sin(pi*(t-i*T)/T);
        dem1=pi*(t-i*T)/T;
        num2=cos(a*pi*(t-i*T)/T);
        dem2=1-(2*a*(t-i*T)/T).^2;
        p=(num1./dem1).*(num2./dem2);
        plot(u,p,'linewidth',3);
    else
        p=zeros(1,length(t));
        plot(u,p);
    end
end
legend('bit','bit2','bit3','bit4','bit5','bit6','bit7','bit7','bit8');
title('Raised cosine pulse');
xlabel('Time in seconds');
ylabel('amplitude in volts');

