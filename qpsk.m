clc;
clear all;
close all;
data=[0 1 0 1 1 1 0 0 1 1];
figure(1)
stem(data,'linewidth',3),grid on;
title('Information before Transmitting');
axis([0 length(data) 0 1]);
data_NZR=2*data-1;
s_p_data=reshape(data_NZR, 2, length(data)/2);
br=10.^6;
f=br;
T=1/br;
t=T/99:T/99:T;
y=[];
y_in=[];
y_qd=[];
for(i=1:length(data)/2)
    y1=s_p_data(1,i)*cos(2*pi*f*t);
    y2=s_p_data(2,i)*sin(2*pi*f*t);
    y_in=[y_in y1];
    y_qd=[y_qd y2];
    y=[y y1+y2];
end
Tx_sig=y;
tt=T/99:T/99:(T*length(data))/2;
figure(2)
subplot(3,1,1);
plot(tt,y_in,'linewidth',3),grid on;
title('waveform for inphase component in QPSK modulation');
xlabel('time(sec)');
ylabel('amplitude(volt)');
subplot(3,1,2);
plot(tt,y_qd,'linewidth',3),grid on;
title('waveform for quadrature component in QPSK modulation');
xlabel('time(sec)');
ylabel('amplitude(volt)');
subplot(3,1,3);
plot(tt,Tx_sig,'linewidth',3),grid on;
title('QPSK modulated signal');
xlabel('time(sec)');
ylabel('amplitude(volt)');
Rx_data=[];
Rx_sig=Tx_sig;
for(i=1:1:length(data)/2)
    Rx_in_data=0;
    Z_in=Rx_sig((i-1)*length(t)+1:i*length(t)).*cos(2*pi*f*t);
    Z_in_intg=(trapz(t,Z_in))*(2/T);
if(Z_in_intg>0)
        Rx_in_data=1;
else
        Rx_qd_data=0;
end
    Z_qd=Rx_sig((i-1)*length(t)+1:i*length(t)).*sin(2*pi*f*t);
    Z_qd_intg=(trapz(t,Z_qd))*(2/T);
if(Z_qd_intg>0)
        Rx_qd_data=1;
else
        Rx_qd_data=0;
end
    Rx_data=[Rx_data Rx_in_data Rx_qd_data];
end
figure(3)
stem(Rx_data,'linewidth',3);
title('information after receiving');
axis([0 length(data) 0 1]);
grid on;
