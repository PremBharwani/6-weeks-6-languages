using BenchmarkTools
V1 = Vector{Any}(undef,10000)
V2 = Vector{Any}(undef,10000)
for i in 1:5000
    V1[i]=rand(1:100)
    V2[i]=rand(1:100)
end
for i in 5001:10000
    V1[i]=100*rand(Float64)
    V2[i]=100*rand(Float64)
end
function f1(x)
    a=4*(x^4) + 9*(x^2) + 10*x + 1
    return a
end
function f2(y)
    a=(y^4) + 3*(y^2) + (9*y) + 2
    return a
end
function Solve1(V1,V2)
    sum=0
    for i in 1:10000
        if V1[i]>V2[i]
            sum+=4*(V1[i]^4) + 9*(V1[i]^2) + 10*V1[i] + 1
        else
            sum+=(V1[i]^4) + 3*(V1[i]^2) + (9*V1[i]) + 2
        end
    end
    return sum
    
end
function Solve2(V1,V2)
    sum=0
    for i in 1:10000
        if V1[i]>V2[i]
            sum+=f1(V1[i])
        else
            sum+=f2(V2[i])
        end
    end
    return sum
    
end
@btime Solve1(V1, V2)
@btime Solve2(V1, V2)
#Solve2 is 2.66 times faster than Solve1