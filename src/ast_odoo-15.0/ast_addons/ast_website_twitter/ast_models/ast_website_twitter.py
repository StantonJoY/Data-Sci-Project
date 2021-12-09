Module(
    body=[
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='requests', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        Assign(
            targets=[Name(id='API_ENDPOINT', ctx=Store())],
            value=Constant(value='https://api.twitter.com', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='API_VERSION', ctx=Store())],
            value=Constant(value='1.1', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='REQUEST_TOKEN_URL', ctx=Store())],
            value=BinOp(
                left=Constant(value='%s/oauth2/token', kind=None),
                op=Mod(),
                right=Name(id='API_ENDPOINT', ctx=Load()),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='REQUEST_FAVORITE_LIST_URL', ctx=Store())],
            value=BinOp(
                left=Constant(value='%s/%s/favorites/list.json', kind=None),
                op=Mod(),
                right=Tuple(
                    elts=[
                        Name(id='API_ENDPOINT', ctx=Load()),
                        Name(id='API_VERSION', ctx=Load()),
                    ],
                    ctx=Load(),
                ),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='URLOPEN_TIMEOUT', ctx=Store())],
            value=Constant(value=10, kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='WebsiteTwitter',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='website', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='twitter_api_key', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Twitter API key', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Twitter API Key', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='twitter_api_secret', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Twitter API secret', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Twitter API Secret', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='twitter_screen_name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Get favorites from this screen name', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_request',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='website', annotation=None, type_comment=None),
                            arg(arg='url', annotation=None, type_comment=None),
                            arg(arg='params', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Send an authenticated request to the Twitter API.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='access_token', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_access_token',
                                    ctx=Load(),
                                ),
                                args=[Name(id='website', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='request', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='requests', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='url', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='params',
                                                value=Name(id='params', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='headers',
                                                value=Dict(
                                                    keys=[Constant(value='Authorization', kind=None)],
                                                    values=[
                                                        BinOp(
                                                            left=Constant(value='Bearer %s', kind=None),
                                                            op=Mod(),
                                                            right=Name(id='access_token', ctx=Load()),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            keyword(
                                                arg='timeout',
                                                value=Name(id='URLOPEN_TIMEOUT', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='raise_for_status',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='json',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='requests', ctx=Load()),
                                        attr='HTTPError',
                                        ctx=Load(),
                                    ),
                                    name='e',
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='debug',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Twitter API request failed with code: %r, msg: %r, content: %r', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='e', ctx=Load()),
                                                            attr='response',
                                                            ctx=Load(),
                                                        ),
                                                        attr='status_code',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='e', ctx=Load()),
                                                            attr='response',
                                                            ctx=Load(),
                                                        ),
                                                        attr='reason',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='e', ctx=Load()),
                                                            attr='response',
                                                            ctx=Load(),
                                                        ),
                                                        attr='content',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Raise(exc=None, cause=None),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_refresh_favorite_tweets',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' called by cron job ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='website', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='website', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='twitter_api_key', kind=None),
                                                    Constant(value='!=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='twitter_api_secret', kind=None),
                                                    Constant(value='!=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='twitter_screen_name', kind=None),
                                                    Constant(value='!=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='debug',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Refreshing tweets for website IDs: %r', kind=None),
                                    Attribute(
                                        value=Name(id='website', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='website', ctx=Load()),
                                    attr='fetch_favorite_tweets',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='fetch_favorite_tweets',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='WebsiteTweets', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='website.twitter.tweet', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tweet_ids', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='website', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id='all', ctx=Load()),
                                            args=[
                                                Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='website', ctx=Load()),
                                                            attr='twitter_api_key',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='website', ctx=Load()),
                                                            attr='twitter_api_secret',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='website', ctx=Load()),
                                                            attr='twitter_screen_name',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='debug',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Skip fetching favorite tweets for unconfigured website %s', kind=None),
                                                    Name(id='website', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Continue(),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='params', ctx=Store())],
                                    value=Dict(
                                        keys=[Constant(value='screen_name', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Name(id='website', ctx=Load()),
                                                attr='twitter_screen_name',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='last_tweet', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='WebsiteTweets', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='website_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='website', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='screen_name', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='website', ctx=Load()),
                                                                attr='twitter_screen_name',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='limit',
                                                value=Constant(value=1, kind=None),
                                            ),
                                            keyword(
                                                arg='order',
                                                value=Constant(value='tweet_id desc', kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='last_tweet', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='params', ctx=Load()),
                                                    slice=Constant(value='since_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='last_tweet', ctx=Load()),
                                                        attr='tweet_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='debug',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Fetching favorite tweets using params %r', kind=None),
                                            Name(id='params', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='response', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_request',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='website', ctx=Load()),
                                            Name(id='REQUEST_FAVORITE_LIST_URL', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='params',
                                                value=Name(id='params', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='tweet_dict', ctx=Store()),
                                    iter=Name(id='response', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='tweet_id', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='tweet_dict', ctx=Load()),
                                                slice=Constant(value='id', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='tweet_ids', ctx=Store())],
                                            value=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='WebsiteTweets', ctx=Load()),
                                                        attr='search',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        List(
                                                            elts=[
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value='tweet_id', kind=None),
                                                                        Constant(value='=', kind=None),
                                                                        Name(id='tweet_id', ctx=Load()),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='tweet_ids', ctx=Load()),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='new_tweet', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='WebsiteTweets', ctx=Load()),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='website_id', kind=None),
                                                                    Constant(value='tweet', kind=None),
                                                                    Constant(value='tweet_id', kind=None),
                                                                    Constant(value='screen_name', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='website', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='json', ctx=Load()),
                                                                            attr='dumps',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='tweet_dict', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                    Name(id='tweet_id', ctx=Load()),
                                                                    Attribute(
                                                                        value=Name(id='website', ctx=Load()),
                                                                        attr='twitter_screen_name',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='debug',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='Found new favorite: %r, %r', kind=None),
                                                            Name(id='tweet_id', ctx=Load()),
                                                            Name(id='tweet_dict', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='tweet_ids', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='new_tweet', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='tweet_ids', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_access_token',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='website', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Obtain a bearer token.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='r', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='requests', ctx=Load()),
                                    attr='post',
                                    ctx=Load(),
                                ),
                                args=[Name(id='REQUEST_TOKEN_URL', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='data',
                                        value=Dict(
                                            keys=[Constant(value='grant_type', kind=None)],
                                            values=[Constant(value='client_credentials', kind=None)],
                                        ),
                                    ),
                                    keyword(
                                        arg='auth',
                                        value=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='website', ctx=Load()),
                                                    attr='twitter_api_key',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='website', ctx=Load()),
                                                    attr='twitter_api_secret',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='timeout',
                                        value=Name(id='URLOPEN_TIMEOUT', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='r', ctx=Load()),
                                    attr='raise_for_status',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='r', ctx=Load()),
                                    attr='json',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='access_token', ctx=Store())],
                            value=Subscript(
                                value=Name(id='data', ctx=Load()),
                                slice=Constant(value='access_token', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='access_token', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
