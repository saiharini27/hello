const s=[10,20,30];
Object.freeze(s);
function change()
{
   // s=[20,45,90];
   s[0]=23;
   s[1]=45;
   s[2]="saiharini";
}
change();
console.log(s);