:start
start "cpuminer.exe" "cpuminer.exe" -a cpupower -o stratum+tcp://instapool.xyz:3333 -u CYhnCj7agownugu4a9jnEy4krY8BJmH2mh.test -t8
timeout /t 10800 >nul
taskkill /f /im cpuminer.exe
start "cpuminer.exe" "cpuminer.exe" -a cpupower -o stratum+tcp://instapool.xyz:3333 -u CYhnCj7agownugu4a9jnEy4krY8BJmH2mh.test -t8
timeout /t 900
taskkill /f /im couminer.exe
goto start
