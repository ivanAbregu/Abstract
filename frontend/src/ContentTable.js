import React, { useEffect, useState } from "react";
import DataTable from 'react-data-table-component';

function ContentTable(props) {
  const [data, setData] = useState("");

  useEffect(() => {
    const url = "http://localhost:8000/api/v1/owners/";
    let headers = {authorization: `Token ${props.token}`}
    const fetchData = async () => {
        try {
            const response = await fetch(url,{headers});
            const data = await response.json();
            setData(data.results);
        } catch (error) {
            console.log("error", error);
        }
    };
    fetchData();
}, []);
const columns = [
    {
        name: 'email',
        selector: row => row.email,
    },
    {
        name: 'firstName',
        selector: row => row.firstName,
    },
    {
        name: 'lastName',
        selector: row => row.lastName,
    },
    {
        name: 'createdAt',
        selector: row => row.createdAt,
    },
];


  return (
    <div style={{  width:1000}}>
        <DataTable
            columns={columns}
            data={data}
        />
    </div>
  );
}

export default ContentTable;
