import React, {useState, useEffect} from 'react';
import axios from 'axios';

function Wallet(){
    // set a number
    const [coins, setCoins] = useState(0)
    // set strings
    const [countChain, setCountChain] = useState('')
    const [transactions, setTransactions] = useState('')
    const [id, setId] = useState('')
    // set true/false
    // const [isOpen, setIsOpen] = useState(false)

    // const [form, setValues] = useState({
    //     id: 0,

    // })
    useEffect(() => {
        axios
        .get('http://localhost:5000/chain')
        .then(response => {
            setCountChain(response.data.countChain)
            setCoins(coins)
            transaction_array = []
       
        response.data.countChain.map(b => {
            transactions.push(b.transaction_array[0])
            console.log('transaction_array', transaction_array)
            console.log('transactions..', transaction)
        })
        setTransactions(transactions)
    })

}, [])

handle_change = e => {
    e.preventDefault()
    console.log('id', id)
    axios.post('http://localhost:5000/user/id', {id: id})
    .then(response => {
        console.log('response in handle_change', response)
    })
}

    return (
        <div>
            <h1>Wallet!</h1>
        </div>
    )
}

export default Wallet