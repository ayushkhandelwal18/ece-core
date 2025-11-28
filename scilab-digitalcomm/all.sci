clc;
clear;
close;


t1 = -6:0.01:6;               
f = 1;                      
A = 3;                      
fs = 1000;                    

u = ones(t1).*(t1>=0);        // Unit step signal
r = t1.*(t1>=0);              // Ramp signal

t = 0:1/fs:10;                // continuous time scale
y = A*sin(2*%pi*f*t);         // continuous sine

N = 1000;
n = 0:N;
y2 = A*sin(2*%pi*f*n/fs);     // discrete sine

N1 = 10;
randomSeq = grand(1, N1, "uin", 1, 100);   // random integer sequence

mu = 0; sigma = 1;
x = -5:0.01:5;
gauss = (1/(sigma*sqrt(2*%pi))) * exp(-((x-mu).^2)/(2*sigma^2));  // gaussian pdf

n2 = -10:10;                  
impulse = double(n2 == 0);    // impulse signal (δ[n])

// Exponential Signal
t_exp = 0:0.01:5;
a = 1;                        
exp_sig = exp(a * t_exp);    

figure();


subplot(3,3,1);
plot(t1,u);
title("Unit Step");
xlabel("t"); ylabel("U(t)");
xgrid();


subplot(3,3,2);
plot(t1,r);
title("Ramp Signal");
xlabel("t"); ylabel("R(t)");
xgrid();


subplot(3,3,3);
plot(t,y);
title("Continuous Sine 1 Hz");
xlabel("Time"); ylabel("Amplitude");
xgrid();


subplot(3,3,4);
plot2d3(n,y2);
title("Discrete Sine 1 Hz");
xlabel("n"); ylabel("Amplitude");
xgrid();


subplot(3,3,5);
plot(1:N1, randomSeq);
title("Random Integer Sequence");
xlabel("n"); ylabel("Value");
xgrid();


subplot(3,3,6);
plot(x,gauss);
title("Gaussian PDF");
xlabel("x"); ylabel("Probability Density");
xgrid();


subplot(3,3,7);
plot2d3(n2, impulse');      
title("Impulse Signal δ[n]");
xlabel("n"); ylabel("δ[n]");
xgrid();

subplot(3,3,8);
plot(t_exp, exp_sig);
title("Exponential Signal e^{at}");
xlabel("t"); ylabel("Amplitude");
xgrid();
