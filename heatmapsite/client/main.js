import { Template } from 'meteor/templating';
import { ReactiveVar } from 'meteor/reactive-var';
import {Session} from 'meteor/session';
import './main.html';

Template.picturebox.onCreated(function (){
  Session.set('picnum', 1);
  return;
})

Template.picturebox.helpers({
  picPath(){
    n = Session.get('picnum');
    return "./d"+ n.toString() + ".jpg"
  }
})

Template.picturebox.events({
  "click .fa-arrow-left" (event){
    num = Session.get('picnum');
    if(num > 1){
      num = num -1;
      Session.set('picnum', num)
    }
  },

  "click .fa-arrow-right" (event){
    num = Session.get('picnum');
    if(num < 2){
      num = num +1;
      Session.set('picnum', num)
    }
  }
})
