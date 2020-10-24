<template>
    <div id = "rank">
        <p class = "rankTitle">Rank</p>
        <b-img center :src="image" v-bind="img_attributes"/>
        <p>{{tier}} {{rank}} {{lp}}</p>
    </div>
</template>

<script>
    export default {
        name: 'rank',
        props: ['tier','rank','lp', 'image'],
        data(){
            return{
                img_attributes: {
                    width: 75,
                    height: 75
                    }
            }
        }
    }
</script>

<style>
    p.rankTitle {
        position: relative;
        
    }
    #rank{
        position: absolute;
        margin: auto;
        width: 150px;
        top:0;
        right:0;
    }
</style> 