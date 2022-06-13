using BenchmarkTools

V1 = Vector{Any}(undef,10000)
V2 = Vector{Any}(undef,10000)
# Populate these 2 vectors with random float and integer values (in the range 1-100) in a ratio close to 1:1. Try to 
# make the Vectors as randomised as possible.
for i in 1:10000
    u = rand()
    if u<0.5
        V1[i] = rand(1:100)
    else
        V1[i] = 1 + 99 * rand()
    end
end
    
for j in 1:10000
    v = rand()
    if v<0.5
        V2[j] = rand(1:100)
    else
        V2[j] = 1 + 99 * rand()
    end
end

function Solve1(V1,V2)
    sum = 0
    for k in 1:10000
      if V1[k] > V2[k]
        x = V1[k]
        sum += 4*(x^4) + 9*(x^2) + 10*x + 1
      else
        y = V2[k]
        sum += y^4 + 3*(y^2) + 9*y + 2
      end
    end
    return sum
end


function Solve2(V1,V2)
    function fx(x::Int64)
      sum = 4*(x^4) + 9*(x^2) + 10*x + 1
      return sum
    end
    function fx(x::Float64)
      sum = 4*(x^4) + 9*(x^2) + 10*x + 1
      return sum
    end
    function fy(y::Int64)
      sum = y^4 + 3*(y^2) + 9*y + 2
      return sum
    end
    function fy(y::Float64)
      sum = y^4 + 3*(y^2) + 9*y + 2
      return sum
    end


    ans = 0
    for i in 1:10000
      if V1[i]>V2[i]
        ans += fx(V1[i])
      else 
        ans += fy(V2[i])
      end
    end

    return ans
end

@btime Solve1(V1,V2)
@btime Solve2(V1,V2)

@btime Solve2(V1,V2)
@btime Solve1(V1,V2)
