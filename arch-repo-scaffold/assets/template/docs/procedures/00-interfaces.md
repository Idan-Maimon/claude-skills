# 00 :: Interfaces and Data Exchange

Every external call the procedures make: the endpoint, a real request, a real response, and the
traps. One numbered section per system. Procedures link here instead of repeating payloads.

<!--
  Section shape (delete this comment once read):

  ## 1 :: <system> — <one-line role>
  ### 1.1 <operation>
  Endpoint, auth, a real request body, a real response, and error codes with what each means
  for the caller.
  ### 1.2 What you cannot do
  Limits and the traps the implementation learned the hard way.

  Example:

  ## 1 :: server-scan — the fleet inventory
  ### 1.1 Draw candidates
  `GET /api/v1/servers?prefix=ocp-c200-mtl&state=available`
  ```json
  [{"serial": "fch2145v1ab", "site": "five", "macs": ["0e:12:..."]}]
  ```
  ### 1.2 Take or extend the install lock
  `409` means two different things: already locked by you (extend) or by someone else (skip).
-->

## 1 :: <System> — <role>

### 1.1 <Operation>
