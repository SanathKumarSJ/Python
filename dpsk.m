clc;
clear all;
N=10^4;
rand('state',100);
randn('state',200);
ip=rand(1,N)>0.5;
ipD=mod(filter(1, [1 -1], ip),2);
s=2*ipD-1;
Eb_No_dB=[-3:10];
nErr_dbpsk_coh=zeros(size(Eb_No_dB));
for ii=1:length(Eb_No_dB)
    noise=1/sqrt(2)*(randn(1,N)+1i*randn(1,N));
    y=s+10^(-Eb_No_dB(ii)/20)*noise;
    ipDHat_coh=real(y)>0;
    ipHat_coh=mod(filter([1 -1],1,ipDHat_coh),2);
    nErr_dbpsk_coh(ii)=sum(ip~=ipHat_coh);
end
SPmBer_dpsk_coh=nErr_dbpsk_coh/N;
theeory_dpsk_coh=erfc(sqrt(10.^(Eb_No_dB/10))).*(1-0.5*erfc(sqrt(10.^(Eb_No_dB/10))));

figure(1)
semilogy(Eb_No_dB, theeory_dpsk_coh,'b-');
hold on;
semilogy(Eb_No_dB,SPmBer_dpsk_coh,'mx-')
axis([-3 10 10^-6 1]);
grid on;
legend('Theory','Simulation');
xlabel('Eb/No (dB)');
ylabel('Bit Error');
title('Bit error probability curve for coherent demodulation of DBPSK');
