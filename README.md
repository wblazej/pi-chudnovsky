# pi-chudnovsky
Python implementation of π digits calculation using [Chudnovsky algorithm](https://en.wikipedia.org/wiki/Chudnovsky_algorithm). This method is one of the most efficient way to calculate π and was used multiple times in breaking world record of π digits calculating.

## Performance
Performance tests showed that the time complexity of the implementation of the algorithm is square. Increase presents how much execution time has raised compared to previous test. The implementation is able to calculate 1 milion digits under 8 minutes.

### Testing commands
```
# powers of 2 test command
python test.py --max 20

# powers of 10 test command
python test.py --dec --min 1 --max 6
```

### Apple M1
Powers of 2
```
digits: 1024    time: 0.523 ms    increase: None
digits: 2048    time: 1.792 ms    increase: 3.427
digits: 4096    time: 6.922 ms    increase: 3.863
digits: 8192    time: 25.601 ms   increase: 3.699
digits: 16384   time: 91.741 ms   increase: 3.583
digits: 32768   time: 377.478 ms  increase: 4.115
digits: 65536   time: 1.599 s     increase: 4.236
digits: 131072  time: 6.742 s     increase: 4.216
digits: 262144  time: 28.286 s    increase: 4.196
digits: 524288  time: 1.982 m     increase: 4.205
digits: 1048576 time: 8.36 m      increase: 4.218
```
Powers of 10
```
digits: 10      time: 0.009 ms    increase: None
digits: 100     time: 0.022 ms    increase: 2.447
digits: 1000    time: 0.38 ms     increase: 17.14
digits: 10000   time: 36.527 ms   increase: 96.114
digits: 100000  time: 3.913 s     increase: 107.114
digits: 1000000 time: 7.6 m       increase: 116.546
```

### ARM-based virtualization
Powers of 2
```
digits: 1024	time: 0.688 ms    increase: None
digits: 2048	time: 1.685 ms    increase: 2.449
digits: 4096	time: 6.751 ms    increase: 4.006
digits: 8192	time: 27.759 ms   increase: 4.112
digits: 16384	time: 116.173 ms  increase: 4.185
digits: 32768	time: 491.369 ms  increase: 4.23
digits: 65536	time: 2.076 s     increase: 4.226
digits: 131072	time: 8.813 s     increase: 4.245
digits: 262144	time: 37.879 s    increase: 4.298
digits: 524288	time: 2.638 m     increase: 4.178
digits: 1048576	time: 11.16 m     increase: 4.231
```
Powers of 10
```
digits: 10	time: 0.035 ms    increase: None
digits: 100	time: 0.024 ms    increase: 0.689
digits: 1000	time: 0.438 ms    increase: 18.02
digits: 10000	time: 44.101 ms   increase: 100.638
digits: 100000	time: 5.126 s     increase: 116.235
digits: 1000000	time: 10.134 m    increase: 118.621
```

### Raspberry Pi 4b
Powers of 2
```
digits: 1024	time: 1.243 ms    increase: None
digits: 2048	time: 4.173 ms    increase: 3.358
digits: 4096	time: 15.679 ms   increase: 3.757
digits: 8192	time: 62.247 ms   increase: 3.97
digits: 16384	time: 259.258 ms  increase: 4.165
digits: 32768	time: 1.11 s      increase: 4.28
digits: 65536	time: 4.641 s     increase: 4.182
digits: 131072	time: 19.59 s     increase: 4.221
digits: 262144	time: 1.411 m     increase: 4.322
digits: 524288	time: 5.868 m     increase: 4.158
digits: 1048576	time: 24.996 m    increase: 4.26
```
Powers of 10
```
digits: 10	time: 0.072 ms    increase: None
digits: 100	time: 0.077 ms    increase: 1.062
digits: 1000	time: 1.137 ms    increase: 14.765
digits: 10000	time: 99.194 ms   increase: 87.241
digits: 100000	time: 11.508 s    increase: 116.015
digits: 1000000	time: 22.854 m    increase: 119.154
```

## API
Endpoitns that returns digits of π.
### Get digits
Endpoint: `https://serverless.wblz.xyz/pi/digits/<count_of_digits>`

`count_of_digits` - how many decimal places of π you want to get (max 1 milion).

Response for https://serverless.wblz.xyz/pi/digits/10:
```
{
  ok: true,
  pi: "1415926535"
}
```
### Range of digits
Endpoint: `https://serverless.wblz.xyz/pi/range/<from>/<to>`

`from` - starting index of the range of digits you want to get

`to` - ending index of the range of digits you want to get (max 1 bilion)

Max range size is 1 milion

Response for https://serverless.wblz.xyz/pi/range/5/10:
```
{
  ok: true,
  pi: "26535"
}
```

## Contribution
Run the testing commands on your CPU and share your results creating a PR to this readme if the CPU is not present here yet.
