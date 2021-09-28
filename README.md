# blockchain-py

A simple blockchain structure to learn how te blockchain works under the hood.
That was only created to educations means, and is a simplification of a actually blockchain

## Endpoints

### `GET /chain`

Get all data stored on the blockchain

### `POST /transaction/new`

add a new transaction to the structure

body:

```json
{
  "sender": "my address",
  "recipient": "someone else's address",
  "amount": 5
}
```

### `GET /mine`

add a new block to the chain with all pending transactions
