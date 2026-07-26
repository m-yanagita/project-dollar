<template>

<div class="container">

    <h1 class="title">

        Project Dollar

    </h1>

    <p class="sub-title">

        Build Useful Tools For Entrepreneurs.

    </p>

    <p>

        Free tools for founders,
        creators and developers worldwide.

    </p>

    <br>

    <NuxtLink to="/name-generator">

        <button class="button">

            Try Now

        </button>

    </NuxtLink>


    <br><br>


    <div class="card">

        <h2>

            Why Project Dollar ?

        </h2>

        <br>

        <p>
            No Signup Required
        </p>

        <p>
            Free To Use
        </p>

        <p>
            New Tools Every Month
        </p>

    </div>


    <br>


    <div class="card">

        <h2>

            Available Tools

        </h2>

        <br>

        <h3>

            Startup Name Generator

        </h3>

        <p>

            Generate startup names instantly.

        </p>

        <br>

        <NuxtLink
        to="/name-generator"
        >

            <button class="button">

                Use Now

            </button>

        </NuxtLink>


    </div>


    <br>


    <div class="card">

        <h2>

            More Tools Coming Soon

        </h2>

        <br>

        <p>SEO Generator</p>

        <p>Password Generator</p>

        <p>Prompt Generator</p>

        <p>UUID Generator</p>

    </div>

</div>

</template>

<style scoped>

.container{
    max-width:800px;
    margin:50px auto;
    padding:30px;
}


.title{
    text-align:center;
    font-size:50px;
}


.sub-title{

    text-align:center;
    color:gray;
    margin-bottom:50px;

}

.card{

    background:white;
    padding:40px;
    border-radius:20px;
    box-shadow:0 0 20px rgba(0,0,0,.1);

}

.button{

    width:100%;
    padding:15px;
    border:none;
    border-radius:10px;
    cursor:pointer;
    font-size:18px;
    background:black;
    color:white;

}

</style>