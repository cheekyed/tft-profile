<template>
    <div id = "profile">
    <b-list-group-item v-bind = "group_item_attr" class = "profile_item ">
        <p class= "summTitle">{{summonerName}}</p>
        <rank 
            :tier = "tier" 
            :rank = "rank"
            :lp = "lp"
            :image = "image"
        >            
        </rank>
    </b-list-group-item>
    </div>
</template>

<script>
    import rank from '@/components/Rank.vue'
    const axios  = require('axios')

    export default {
        name: 'profile',
        components:{
            rank
        },
        mounted(){
            var self = this
            axios.get('http://localhost:5000/api/profile')
            .then (function(response){
                console.log(response)
                self.loading = false
                self.summonerName = response.data['SummonerName']
                self.profileIconId = response.data['ProfileIconId']
                self.tier = response.data['Tier']
                self.lp = response.data['Lp'] + 'LP'
                if (self.tier == 'Unranked'){
                    self.image = '../static/unranked.png'
                    }
                    else{
                        self.image = '../static/tier/Emblem_'+`${self.tier.toLowerCase().charAt(0).toUpperCase()+self.tier.slice(1).toLowerCase()}.png`
                    }                
            })            
        },
        data(){
            return{
                group_item_attr:{
                    variant: 'danger'
                },
                image: '',
                rank:'',
                tier: '',
                lp:'',
                summonerName: '',
                profileIcon: '',
            }
        }
    }
</script>

<style>
    .summTitle{
        position: absolute;
        top: 0;
        left: 0;
    }
    .profile_item{
        width: 100%;
        height: 15%;
    }
</style> 