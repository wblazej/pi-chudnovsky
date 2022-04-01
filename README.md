# pi-chudnovsky
Python implementation of π digits calculation using [Chudnovsky algorithm](https://en.wikipedia.org/wiki/Chudnovsky_algorithm). This method is one of the most efficient way to calculate π and was used to break π digits calculating world record multiple times.

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
