# fasta-profiler

Print report of the frequency of each amino acid in the FASTA file.

How to Run:
-----------
1. Clone this repository:
    ```shell
    git clone https://github.com/mriffle/fasta-profiler.git
    ```

2. Install requirements:
    ```shell
    pip3 install -r requirements.txt
    ```

3. Run script with:
    ```shell
    python3 fasta-profiler.py /path/to/file.fasta
    ```

Example output:
```
Profile for: /path/to/file.fasta
        Total residues: 11398263
        Totals for each amino acid code:
                AA      count   frac
                --      -----   ----
                A       799341  0.070128
                C       262784  0.023055
                D       540074  0.047382
                E       809609  0.071029
                F       415977  0.036495
                G       749941  0.065794
                H       298599  0.026197
                I       494600  0.043393
                K       653329  0.057318
                L       1135355 0.099608
                M       242886  0.021309
                N       409468  0.035924
                P       719141  0.063092
                Q       543435  0.047677
                R       642276  0.056349
                S       949187  0.083275
                T       609768  0.053497
                U       36      3e-06
                V       680069  0.059664
                W       138512  0.012152
                Y       303876  0.02666
```
