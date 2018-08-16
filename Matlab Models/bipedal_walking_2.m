%dimensions of the leg links
L1 = 0.135;
L2 = 0.155;

%DH Factors
links(1) = Link([    0       0    L1   0], 'standard');
links(2) = Link([    0       0    L2   0], 'standard');

%a single leg
leg = SerialLink(links, 'name', 'leg', 'offset', [0   0  0]);

% define the rectangular path taken by the foot
path = [20 -5 0; 16 0 0; 16 1 0; 20 5 0; 20 -5 0 ]*0.01;
  
timeseg = [0.5 1.5 1.5 1.5 5.0]';

y = mstraj(path, [], timeseg, path(1,:), 0.1, 0);

qcycle = leg.ikine( transl(y), [], [1 1 0 0 0 0] );

%dimensions of the robot's rectangular body, width(W) and height(H),
%the legs are at sides and middle.
W = 0.1; L = 0.05;

plotopt = leg.plot({'noraise', 'nobase', 'noshadow', ...
    'nowrist', 'nojaxes'});

% create 2 leg robot.  Each leg is a clone of the leg robot we built above,
legs(1) = SerialLink(leg, 'name', 'leg1', 'base', transl(0, 0, 0)*troty(pi/2)*trotx(pi/2));
legs(2) = SerialLink(leg, 'name', 'leg2', 'base', transl(0, -W, 0)*troty(pi/2)*trotx(pi/2));

% create a fixed size axis for the robot, and set z positive downward
clf; axis([-0.3 0.1 -0.2 0.2 -0.15 0.05]);
hold on

% draw the robot's body
patch([0 0 0 0], [0 -W 0 -W], [0 -L 0 -L], ...
    'FaceColor', 'r', 'FaceAlpha', 0.5)

% instantiate each robot in the axes
for i=1:2
    legs(i).plot(qcycle(1,:), plotopt);
end
hold off

% walk!
k = 1;
while 1
    legs(1).plot( gait(qcycle, k, 0,   0), plotopt);
    legs(2).plot( gait(qcycle, k, 50, 0), plotopt);
    drawnow
    k = k+1;
end
