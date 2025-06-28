| Interface | Meaning  | Notes                          |
| --------- | -------- | ------------------------------ |
| `lo`      | Loopback | Local traffic only             |
| `enp1s0`  | Ethernet | Likely disconnected            |
| `wlo1`    | Wi-Fi    | Wireless network               |
tem mais códigozinhos lol

IGNORAR O O1, BUSCAR APENAS WL (wireless network) pq o número pode mudar dependendo de pci

EU NÃO ACHO QUE WL É UMA TAG OBRIGATÓRIA, PROCURAR POR ELA EM UM TRY CATCH

Bytes / Packets pra descobrir o tamanho médio dos pacotes enviados e recebidos (idealmente fazer isso depois de já ter feito o cálculo de quantos pacotes foram no último segundo duhr, don't be stupid david)
