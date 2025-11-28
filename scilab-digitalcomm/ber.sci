clc; clear; close;

N = 100000;                    
bits = grand(1, N, "uin", 0, 1);

bpsk = 2*bits - 1;             

EbN0_dB = 0:1:12;             
BER_sim = zeros(1, length(EbN0_dB));
BER_theory = zeros(1, length(EbN0_dB));

for i = 1:length(EbN0_dB)
    
    EbN0 = 10^(EbN0_dB(i)/10);  
    noise_var = 1/(2*EbN0);
    
    noise = sqrt(noise_var)*rand(1, N, "normal");
    r = bpsk + noise;         
    
    detected = r > 0;         
    
    errors = sum(bits <> detected);
    BER_sim(i) = errors / N;
    
    BER_theory(i) = 0.5 * erfc(sqrt(EbN0)); 
end


figure();
semilogy(EbN0_dB, BER_sim, 'o-');
plot(EbN0_dB, BER_theory, 'r-');
legend(["Simulated BER", "Theoretical BER"]);
xlabel("Eb/No (dB)");
ylabel("Bit Error Rate (BER)");
title("BER vs Eb/No for BPSK");
xgrid();
