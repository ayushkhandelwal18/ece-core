clc;
clear;
close;

bits = [1 0 1 1 0];
n = length(bits);
bit_duration = 1;
A = 1; 

t = 0:0.001:n;

input_signal = [];
bipolarnrz = [];
bipolarrz = [];
manchester = [];

last_polarity = -A; 


for i = 1:n
    if bits(i) == 1 then
       
        input_signal = [input_signal ones(1,1000)];

        // bipolar
        last_polarity = -last_polarity;
        bipolarnrz = [bipolarnrz last_polarity*ones(1,1000)];
        bipolarrz = [bipolarrz last_polarity*ones(1,500) zeros(1,500)];

        // Manchester
        manchester = [manchester A*ones(1,500) -A*ones(1,500)];
    else
        
        input_signal = [input_signal zeros(1,1000)];

        // Bipolar
        bipolarnrz = [bipolarnrz zeros(1,1000)];
        bipolarrz = [bipolarrz zeros(1,1000)];

        // Manchester
        manchester = [manchester -A*ones(1,500) A*ones(1,500)];
    end
end

t = 0:0.001:bit_duration*n-0.001;

clf();
subplot(4,1,1);
plot(t,input_signal);
xtitle("Input Bit Sequence (10110)","Time","Amplitude");
xgrid();

subplot(4,1,2);
plot(t,bipolarnrz);
xtitle("Bipolar NRZ","Time","Amplitude");
xgrid();

subplot(4,1,3);
plot(t,bipolarrz);
xtitle("Bipolar RZ","Time","Amplitude");
xgrid();

subplot(4,1,4);
plot(t,manchester);
xtitle("Manchester","Time","Amplitude");
xgrid();
