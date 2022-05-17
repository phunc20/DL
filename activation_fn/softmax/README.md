
```julia
function mysoftmax(v; base=ℯ)
    baseᵛ = @. float(base) ^ v
    return baseᵛ ./ sum(baseᵛ)
end
```

```julia
julia> mysoftmax([1,2,3,4]; base=999)
4-element Vector{Float64}:
 1.002001999995992e-9
 1.000999997995996e-6
 0.000999998997998
 0.998998999000002

julia> mysoftmax([1,2,3,4]; base=1.01)
4-element Vector{Float64}:
 0.24628109391166048
 0.24874390485077708
 0.2512313438992848
 0.2537436573382777

julia> mysoftmax([1,2,3,4]; base=1.1)
4-element Vector{Float64}:
 0.2154708037060978
 0.2370178840767076
 0.2607196724843784
 0.28679163973281624

julia> mysoftmax(-4:-1; base=1.1)
4-element Vector{Float64}:
 0.21547080370609778
 0.2370178840767076
 0.2607196724843784
 0.28679163973281624
```
