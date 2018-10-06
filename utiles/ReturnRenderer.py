


from rest_framework.renderers import  JSONRenderer

class MYJSONRenderer(JSONRenderer):
    '''
    需要返回这种：
    {
        code:0,
        msg:'请求成功',
        data:''
    }
    '''


    def render(self, data, accepted_media_type=None, renderer_context=None):
        if isinstance(data,dict):
            code=data.pop('code',0)
            msg=data.pop('msg','请求成功')

        else:
            code=0
            msg='请求成功'

        res={
            'code':code,
            'msg':msg,
            'data':data
        }

        return super().render(res,accepted_media_type=None,renderer_context=None)