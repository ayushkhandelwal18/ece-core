clc;
clear;
close;

bits = [1 0 1 1 0];
n = length(bits);
bit_duration = 1;

t = 0:0.001:n;

input_signal = [];
unrz = [];
urz = [];
pnrz = [];
prz = [];

for i = 1:n
   
    if bits(i) == 1 then
        
        input_signal = [input_signal ones(1,1000)];
        
        //Unipolar
        unrz = [unrz ones(1,1000)];
        urz = [urz ones(1,500) zeros(1,500)];

        //Polar
        pnrz = [pnrz ones(1,1000)];
        prz = [prz ones(1,500) zeros(1,500)];

    else
        
        input_signal = [input_signal zeros(1,1000)];// Input 0

        // Unipolar
        unrz = [unrz zeros(1,1000)];
         urz = [ urz zeros(1,1000)];

        //Polar
        pnrz = [pnrz -ones(1,1000)];
        prz = [prz -ones(1,500) zeros(1,500)];

    end
end


t = 0:0.001:bit_duration*n-0.001;

// Plotting
clf();
subplot(3,2,1);
plot(t,input_signal);
xtitle("Input Bit Sequence (10110)","Time","Amplitude");
xgrid();

subplot(3,2,3);
plot(t,unrz);
xtitle("Unipolar NRZ","Time","Amplitude");
xgrid();

subplot(3,2,4);
plot(t,unrz);
xtitle("Unipolar RZ","Time","Amplitude");
xgrid();

subplot(3,2,5);
plot(t,pnrz);
xtitle("Polar NRZ","Time","Amplitude");
xgrid();

subplot(3,2,6);
plot(t,prz);
xtitle("Polar RZ","Time","Amplitude");
xgrid();
