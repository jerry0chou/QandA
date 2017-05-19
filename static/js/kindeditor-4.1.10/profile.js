KindEditor.ready(function (K) {
    K.create('textarea[name=profile]', {
         width: '300px',
        height: '300px',
        uploadJson: '/admin/upload/kindeditor',
        items:["image"]
    });

});